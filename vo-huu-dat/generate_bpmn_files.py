from __future__ import annotations

import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


BPMN_NS = "http://www.omg.org/spec/BPMN/20100524/MODEL"
BPMNDI_NS = "http://www.omg.org/spec/BPMN/20100524/DI"
DC_NS = "http://www.omg.org/spec/DD/20100524/DC"
DI_NS = "http://www.omg.org/spec/DD/20100524/DI"


for prefix, uri in {
    "bpmn": BPMN_NS,
    "bpmndi": BPMNDI_NS,
    "dc": DC_NS,
    "di": DI_NS,
}.items():
    ET.register_namespace(prefix, uri)


def qname(ns: str, tag: str) -> str:
    return f"{{{ns}}}{tag}"


@dataclass
class Node:
    node_id: str
    kind: str
    name: str
    lane: str
    col: int
    width: int = 120
    height: int = 70

    @property
    def shape_size(self) -> tuple[int, int]:
        if self.kind in {"startEvent", "endEvent", "intermediateCatchEvent"}:
            return (36, 36)
        if self.kind == "exclusiveGateway":
            return (50, 50)
        return (self.width, self.height)


def add_text_el(parent, tag, text):
    el = ET.SubElement(parent, qname(BPMN_NS, tag))
    el.text = text
    return el


def prettify(elem: ET.Element) -> None:
    ET.indent(elem, space="  ")


def build_process_file(
    *,
    file_path: Path,
    definitions_id: str,
    collaboration_id: str,
    process_id: str,
    participant_company_id: str,
    participant_external_id: str,
    participant_company_name: str,
    participant_external_name: str,
    lanes: list[tuple[str, str]],
    ext_process_id: str,
    ext_nodes: list[Node],
    ext_sequence: list[tuple[str, str, str | None]],
    ext_message_nodes: dict[str, str],
    nodes: list[Node],
    sequence_flows: list[tuple[str, str, str, str | None]],
    message_flows: list[tuple[str, str, str, str | None]],
):
    definitions = ET.Element(
        qname(BPMN_NS, "definitions"),
        {
            "id": definitions_id,
            "targetNamespace": "http://bpmn.io/schema/bpmn",
            "exporter": "Codex",
            "exporterVersion": "1.0",
        },
    )

    collaboration = ET.SubElement(definitions, qname(BPMN_NS, "collaboration"), {"id": collaboration_id})
    ET.SubElement(
        collaboration,
        qname(BPMN_NS, "participant"),
        {"id": participant_company_id, "name": participant_company_name, "processRef": process_id},
    )
    ET.SubElement(
        collaboration,
        qname(BPMN_NS, "participant"),
        {"id": participant_external_id, "name": participant_external_name, "processRef": ext_process_id},
    )

    for mf_id, src, tgt, name in message_flows:
        attrs = {"id": mf_id, "sourceRef": src, "targetRef": tgt}
        if name:
            attrs["name"] = name
        ET.SubElement(collaboration, qname(BPMN_NS, "messageFlow"), attrs)

    process = ET.SubElement(definitions, qname(BPMN_NS, "process"), {"id": process_id, "isExecutable": "false"})
    lane_set = ET.SubElement(process, qname(BPMN_NS, "laneSet"), {"id": f"LaneSet_{process_id}"})
    lane_nodes = {lane_id: [] for lane_id, _ in lanes}
    for node in nodes:
        lane_nodes[node.lane].append(node.node_id)
    for lane_id, lane_name in lanes:
        lane_el = ET.SubElement(lane_set, qname(BPMN_NS, "lane"), {"id": lane_id, "name": lane_name})
        for node_id in lane_nodes[lane_id]:
            add_text_el(lane_el, "flowNodeRef", node_id)

    nodes_by_id = {node.node_id: node for node in nodes}
    incoming: dict[str, list[str]] = {node.node_id: [] for node in nodes}
    outgoing: dict[str, list[str]] = {node.node_id: [] for node in nodes}
    for flow_id, src, tgt, _name in sequence_flows:
        outgoing[src].append(flow_id)
        incoming[tgt].append(flow_id)

    for node in nodes:
        attrs = {"id": node.node_id}
        if node.name:
            attrs["name"] = node.name
        node_el = ET.SubElement(process, qname(BPMN_NS, node.kind), attrs)
        for flow_id in incoming[node.node_id]:
            add_text_el(node_el, "incoming", flow_id)
        for flow_id in outgoing[node.node_id]:
            add_text_el(node_el, "outgoing", flow_id)
        if node.kind == "intermediateCatchEvent":
            ET.SubElement(node_el, qname(BPMN_NS, "messageEventDefinition"), {"id": f"MessageDef_{node.node_id}"})

    for flow_id, src, tgt, name in sequence_flows:
        attrs = {"id": flow_id, "sourceRef": src, "targetRef": tgt}
        if name:
            attrs["name"] = name
        ET.SubElement(process, qname(BPMN_NS, "sequenceFlow"), attrs)

    ext_process = ET.SubElement(definitions, qname(BPMN_NS, "process"), {"id": ext_process_id, "isExecutable": "false"})
    ext_incoming: dict[str, list[str]] = {node.node_id: [] for node in ext_nodes}
    ext_outgoing: dict[str, list[str]] = {node.node_id: [] for node in ext_nodes}
    for flow_id, src, tgt, _name in ext_sequence:
        ext_outgoing[src].append(flow_id)
        ext_incoming[tgt].append(flow_id)
    for node in ext_nodes:
        attrs = {"id": node.node_id}
        if node.name:
            attrs["name"] = node.name
        node_el = ET.SubElement(ext_process, qname(BPMN_NS, node.kind), attrs)
        for flow_id in ext_incoming[node.node_id]:
            add_text_el(node_el, "incoming", flow_id)
        for flow_id in ext_outgoing[node.node_id]:
            add_text_el(node_el, "outgoing", flow_id)
        if node.kind == "intermediateCatchEvent":
            ET.SubElement(node_el, qname(BPMN_NS, "messageEventDefinition"), {"id": f"MessageDef_{node.node_id}"})
    for flow_id, src, tgt, name in ext_sequence:
        attrs = {"id": flow_id, "sourceRef": src, "targetRef": tgt}
        if name:
            attrs["name"] = name
        ET.SubElement(ext_process, qname(BPMN_NS, "sequenceFlow"), attrs)

    # DI layout
    diagram = ET.SubElement(definitions, qname(BPMNDI_NS, "BPMNDiagram"), {"id": f"Diagram_{process_id}"})
    plane = ET.SubElement(diagram, qname(BPMNDI_NS, "BPMNPlane"), {"id": f"Plane_{process_id}", "bpmnElement": collaboration_id})

    company_x = 120
    company_y = 80
    lane_height = 150
    company_width = 2400
    company_height = lane_height * len(lanes)
    ext_x = 120
    ext_y = company_y + company_height + 80
    ext_height = 180
    ext_width = company_width

    ET.SubElement(
        plane,
        qname(BPMNDI_NS, "BPMNShape"),
        {"id": f"{participant_company_id}_di", "bpmnElement": participant_company_id, "isHorizontal": "true"},
    ).append(ET.Element(qname(DC_NS, "Bounds"), {"x": str(company_x), "y": str(company_y), "width": str(company_width), "height": str(company_height)}))
    ET.SubElement(
        plane,
        qname(BPMNDI_NS, "BPMNShape"),
        {"id": f"{participant_external_id}_di", "bpmnElement": participant_external_id, "isHorizontal": "true"},
    ).append(ET.Element(qname(DC_NS, "Bounds"), {"x": str(ext_x), "y": str(ext_y), "width": str(ext_width), "height": str(ext_height)}))

    lane_y = {}
    current_y = company_y
    for lane_id, _lane_name in lanes:
        lane_y[lane_id] = current_y
        lane_shape = ET.SubElement(plane, qname(BPMNDI_NS, "BPMNShape"), {"id": f"{lane_id}_di", "bpmnElement": lane_id, "isHorizontal": "true"})
        lane_shape.append(ET.Element(qname(DC_NS, "Bounds"), {"x": str(company_x + 30), "y": str(current_y), "width": str(company_width - 30), "height": str(lane_height)}))
        current_y += lane_height

    positions: dict[str, tuple[int, int, int, int]] = {}
    start_x = company_x + 120
    col_gap = 180
    for node in nodes:
        w, h = node.shape_size
        x = start_x + node.col * col_gap
        y = lane_y[node.lane] + (lane_height - h) // 2
        positions[node.node_id] = (x, y, w, h)
        shape = ET.SubElement(plane, qname(BPMNDI_NS, "BPMNShape"), {"id": f"{node.node_id}_di", "bpmnElement": node.node_id})
        shape.append(ET.Element(qname(DC_NS, "Bounds"), {"x": str(x), "y": str(y), "width": str(w), "height": str(h)}))

    ext_positions: dict[str, tuple[int, int, int, int]] = {}
    ext_start_x = ext_x + 140
    for node in ext_nodes:
        w, h = node.shape_size
        x = ext_start_x + node.col * 220
        y = ext_y + (ext_height - h) // 2
        ext_positions[node.node_id] = (x, y, w, h)
        shape = ET.SubElement(plane, qname(BPMNDI_NS, "BPMNShape"), {"id": f"{node.node_id}_di", "bpmnElement": node.node_id})
        shape.append(ET.Element(qname(DC_NS, "Bounds"), {"x": str(x), "y": str(y), "width": str(w), "height": str(h)}))

    def center_right(pos):
        x, y, w, h = pos
        return (x + w, y + h // 2)

    def center_left(pos):
        x, y, _w, h = pos
        return (x, y + h // 2)

    def bottom_center(pos):
        x, y, w, h = pos
        return (x + w // 2, y + h)

    def top_center(pos):
        x, y, w, _h = pos
        return (x + w // 2, y)

    for flow_id, src, tgt, _name in sequence_flows:
        edge = ET.SubElement(plane, qname(BPMNDI_NS, "BPMNEdge"), {"id": f"{flow_id}_di", "bpmnElement": flow_id})
        src_pos = positions[src]
        tgt_pos = positions[tgt]
        for x, y in [center_right(src_pos), center_left(tgt_pos)]:
            edge.append(ET.Element(qname(DI_NS, "waypoint"), {"x": str(x), "y": str(y)}))

    for flow_id, src, tgt, _name in ext_sequence:
        edge = ET.SubElement(plane, qname(BPMNDI_NS, "BPMNEdge"), {"id": f"{flow_id}_di", "bpmnElement": flow_id})
        src_pos = ext_positions[src]
        tgt_pos = ext_positions[tgt]
        for x, y in [center_right(src_pos), center_left(tgt_pos)]:
            edge.append(ET.Element(qname(DI_NS, "waypoint"), {"x": str(x), "y": str(y)}))

    lookup = {**positions, **ext_positions}
    for mf_id, src, tgt, _name in message_flows:
        edge = ET.SubElement(plane, qname(BPMNDI_NS, "BPMNEdge"), {"id": f"{mf_id}_di", "bpmnElement": mf_id})
        src_pos = lookup[src]
        tgt_pos = lookup[tgt]
        for x, y in [bottom_center(src_pos), top_center(tgt_pos)]:
            edge.append(ET.Element(qname(DI_NS, "waypoint"), {"x": str(x), "y": str(y)}))

    prettify(definitions)
    file_path.write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(definitions, encoding="unicode"))


def generate_p10(base: Path) -> None:
    lanes = [
        ("Lane_Requester", "Requester / PM"),
        ("Lane_Manager", "Line Manager"),
        ("Lane_IT", "IT Asset Officer / IT Admin"),
        ("Lane_Finance", "Finance - Accounting"),
        ("Lane_Proc", "Procurement"),
        ("Lane_Warehouse", "Warehouse / IT Support"),
    ]
    nodes = [
        Node("Start_P10", "startEvent", "", "Lane_Requester", 0),
        Node("Task_P10_CreateRequest", "task", "Tao ticket yeu cau cap phat / mua sam", "Lane_Requester", 1),
        Node("Task_P10_ApproveNeed", "task", "Phe duyet nhu cau", "Lane_Manager", 2),
        Node("Task_P10_CheckInventory", "task", "Kiem tra ton kho va cau hinh chuan", "Lane_IT", 3),
        Node("Gateway_P10_InStock", "exclusiveGateway", "Con tai san phu hop?", "Lane_IT", 4),
        Node("Task_P10_PrepareAsset", "task", "Cai dat OS, phan mem va chinh sach bao mat", "Lane_IT", 5),
        Node("Task_P10_BudgetApproval", "task", "Phe duyet ngan sach PR", "Lane_Finance", 5),
        Node("Task_P10_GetQuotes", "task", "Lay 3 bao gia va de xuat vendor", "Lane_Proc", 6),
        Node("Task_P10_IssuePO", "task", "Phat hanh PO / ky hop dong", "Lane_Proc", 7),
        Node("Task_P10_InspectGoods", "task", "Nhan hang, kiem dinh cau hinh", "Lane_Warehouse", 8),
        Node("Task_P10_RegisterAsset", "task", "Dan Asset Tag va cap nhat Snipe-IT/CMDB", "Lane_IT", 9),
        Node("Task_P10_Handover", "task", "Ban giao tai san va ky bien ban", "Lane_Warehouse", 10),
        Node("Task_P10_Maintain", "task", "Theo doi su dung, bao tri va kiem ke dinh ky", "Lane_IT", 11),
        Node("Gateway_P10_Dispose", "exclusiveGateway", "Tai san het khau hao / hong nang?", "Lane_IT", 12),
        Node("Task_P10_Disposal", "task", "Thu hoi, xoa du lieu va thanh ly", "Lane_IT", 13),
        Node("End_P10", "endEvent", "", "Lane_IT", 14),
    ]
    sequence = [
        ("Flow_P10_1", "Start_P10", "Task_P10_CreateRequest", None),
        ("Flow_P10_2", "Task_P10_CreateRequest", "Task_P10_ApproveNeed", None),
        ("Flow_P10_3", "Task_P10_ApproveNeed", "Task_P10_CheckInventory", None),
        ("Flow_P10_4", "Task_P10_CheckInventory", "Gateway_P10_InStock", None),
        ("Flow_P10_5", "Gateway_P10_InStock", "Task_P10_PrepareAsset", "Co"),
        ("Flow_P10_6", "Gateway_P10_InStock", "Task_P10_BudgetApproval", "Khong"),
        ("Flow_P10_7", "Task_P10_BudgetApproval", "Task_P10_GetQuotes", None),
        ("Flow_P10_8", "Task_P10_GetQuotes", "Task_P10_IssuePO", None),
        ("Flow_P10_9", "Task_P10_IssuePO", "Task_P10_InspectGoods", None),
        ("Flow_P10_10", "Task_P10_InspectGoods", "Task_P10_RegisterAsset", None),
        ("Flow_P10_11", "Task_P10_PrepareAsset", "Task_P10_Handover", None),
        ("Flow_P10_12", "Task_P10_RegisterAsset", "Task_P10_Handover", None),
        ("Flow_P10_13", "Task_P10_Handover", "Task_P10_Maintain", None),
        ("Flow_P10_14", "Task_P10_Maintain", "Gateway_P10_Dispose", None),
        ("Flow_P10_15", "Gateway_P10_Dispose", "Task_P10_Disposal", "Co"),
        ("Flow_P10_16", "Gateway_P10_Dispose", "End_P10", "Khong"),
        ("Flow_P10_17", "Task_P10_Disposal", "End_P10", None),
    ]
    ext_nodes = [
        Node("Start_Vendor", "startEvent", "", "", 0),
        Node("Task_Vendor_ReceivePO", "task", "Nhan PO va xac nhan don hang", "", 1),
        Node("Task_Vendor_Deliver", "task", "Giao thiet bi / tai lieu bao hanh", "", 2),
        Node("End_Vendor", "endEvent", "", "", 3),
    ]
    ext_sequence = [
        ("Flow_Vendor_1", "Start_Vendor", "Task_Vendor_ReceivePO", None),
        ("Flow_Vendor_2", "Task_Vendor_ReceivePO", "Task_Vendor_Deliver", None),
        ("Flow_Vendor_3", "Task_Vendor_Deliver", "End_Vendor", None),
    ]
    message_flows = [
        ("Message_P10_PO", "Task_P10_IssuePO", "Task_Vendor_ReceivePO", "PO / hop dong mua sam"),
        ("Message_P10_Delivery", "Task_Vendor_Deliver", "Task_P10_InspectGoods", "Thiet bi duoc giao"),
    ]
    build_process_file(
        file_path=base / "P10_mua_sam_va_quan_ly_tai_san_CNTT.bpmn",
        definitions_id="Definitions_P10",
        collaboration_id="Collaboration_P10",
        process_id="Process_P10",
        participant_company_id="Participant_P10_Company",
        participant_external_id="Participant_P10_Vendor",
        participant_company_name="Cong ty phan mem",
        participant_external_name="Vendor",
        lanes=lanes,
        ext_process_id="Process_P10_Vendor",
        ext_nodes=ext_nodes,
        ext_sequence=ext_sequence,
        ext_message_nodes={},
        nodes=nodes,
        sequence_flows=sequence,
        message_flows=message_flows,
    )


def generate_p07(base: Path) -> None:
    lanes = [
        ("Lane_L1", "L1 Support"),
        ("Lane_L2L3", "L2 / L3 Support"),
        ("Lane_QA", "QA / QC"),
        ("Lane_DevOps", "DevOps"),
        ("Lane_SDM", "Service Delivery Manager"),
    ]
    nodes = [
        Node("Start_P07", "intermediateCatchEvent", "Ticket duoc tiep nhan", "Lane_L1", 0),
        Node("Task_P07_Triage", "task", "Kiem tra thong tin va phan loai muc do uu tien", "Lane_L1", 1),
        Node("Task_P07_FirstResponse", "task", "Phan hoi dau tien theo SLA", "Lane_L1", 2),
        Node("Gateway_P07_L1Resolve", "exclusiveGateway", "L1 tu xu ly duoc?", "Lane_L1", 3),
        Node("Task_P07_L1Resolve", "task", "Huong dan / xu ly loi co ban", "Lane_L1", 4),
        Node("Task_P07_Escalate", "task", "Escalate ticket sang L2/L3", "Lane_L1", 4),
        Node("Task_P07_Investigate", "task", "Phan tich log va tai hien loi", "Lane_L2L3", 5),
        Node("Task_P07_Fix", "task", "Sua loi / tao patch hoac workaround", "Lane_L2L3", 6),
        Node("Task_P07_Test", "task", "Regression test tren Staging / UAT", "Lane_QA", 7),
        Node("Task_P07_Deploy", "task", "Deploy patch len Production", "Lane_DevOps", 8),
        Node("Task_P07_Notify", "task", "Gui thong bao va yeu cau khach hang kiem nghiem", "Lane_SDM", 9),
        Node("Start_P07_Verify", "intermediateCatchEvent", "Khach hang phan hoi", "Lane_SDM", 10),
        Node("Gateway_P07_Verified", "exclusiveGateway", "Khach hang xac nhan da dat?", "Lane_SDM", 11),
        Node("Task_P07_Close", "task", "Dong ticket va cap nhat knowledge base", "Lane_L1", 12),
        Node("End_P07", "endEvent", "", "Lane_L1", 13),
    ]
    sequence = [
        ("Flow_P07_1", "Start_P07", "Task_P07_Triage", None),
        ("Flow_P07_2", "Task_P07_Triage", "Task_P07_FirstResponse", None),
        ("Flow_P07_3", "Task_P07_FirstResponse", "Gateway_P07_L1Resolve", None),
        ("Flow_P07_4", "Gateway_P07_L1Resolve", "Task_P07_L1Resolve", "Co"),
        ("Flow_P07_5", "Gateway_P07_L1Resolve", "Task_P07_Escalate", "Khong"),
        ("Flow_P07_6", "Task_P07_Escalate", "Task_P07_Investigate", None),
        ("Flow_P07_7", "Task_P07_Investigate", "Task_P07_Fix", None),
        ("Flow_P07_8", "Task_P07_Fix", "Task_P07_Test", None),
        ("Flow_P07_9", "Task_P07_Test", "Task_P07_Deploy", None),
        ("Flow_P07_10", "Task_P07_Deploy", "Task_P07_Notify", None),
        ("Flow_P07_11", "Task_P07_L1Resolve", "Task_P07_Notify", None),
        ("Flow_P07_12", "Task_P07_Notify", "Start_P07_Verify", None),
        ("Flow_P07_13", "Start_P07_Verify", "Gateway_P07_Verified", None),
        ("Flow_P07_14", "Gateway_P07_Verified", "Task_P07_Close", "Co"),
        ("Flow_P07_15", "Gateway_P07_Verified", "Task_P07_Escalate", "Khong, can xu ly tiep"),
        ("Flow_P07_16", "Task_P07_Close", "End_P07", None),
    ]
    ext_nodes = [
        Node("Start_Client", "startEvent", "", "", 0),
        Node("Task_Client_CreateTicket", "task", "Tao ticket / gui yeu cau ho tro", "", 1),
        Node("Catch_Client_Response", "intermediateCatchEvent", "Nhan phan hoi xu ly", "", 2),
        Node("Task_Client_Verify", "task", "Kiem nghiem va phan hoi ket qua", "", 3),
        Node("End_Client", "endEvent", "", "", 4),
    ]
    ext_sequence = [
        ("Flow_Client_1", "Start_Client", "Task_Client_CreateTicket", None),
        ("Flow_Client_2", "Task_Client_CreateTicket", "Catch_Client_Response", None),
        ("Flow_Client_3", "Catch_Client_Response", "Task_Client_Verify", None),
        ("Flow_Client_4", "Task_Client_Verify", "End_Client", None),
    ]
    message_flows = [
        ("Message_P07_Ticket", "Task_Client_CreateTicket", "Start_P07", "Ticket ho tro"),
        ("Message_P07_Response", "Task_P07_Notify", "Catch_Client_Response", "Thong bao da xu ly"),
        ("Message_P07_Verify", "Task_Client_Verify", "Start_P07_Verify", "Ket qua kiem nghiem"),
    ]
    build_process_file(
        file_path=base / "P07_bao_hanh_va_ho_tro_khach_hang.bpmn",
        definitions_id="Definitions_P07",
        collaboration_id="Collaboration_P07",
        process_id="Process_P07",
        participant_company_id="Participant_P07_Company",
        participant_external_id="Participant_P07_Client",
        participant_company_name="Don vi cung cap dich vu",
        participant_external_name="Khach hang",
        lanes=lanes,
        ext_process_id="Process_P07_Client",
        ext_nodes=ext_nodes,
        ext_sequence=ext_sequence,
        ext_message_nodes={},
        nodes=nodes,
        sequence_flows=sequence,
        message_flows=message_flows,
    )


def main() -> None:
    base = Path(r"D:\DAT-IT\FREELANCE\New folder\business-process-management\vo-huu-dat")
    generate_p10(base)
    generate_p07(base)


if __name__ == "__main__":
    main()
