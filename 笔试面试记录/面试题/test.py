"""
run_test(execution_id, case_id) -> "Pass" | "Fail" | "Timeout"
 
collect_logs(execution_id) -> list[str]
# 返回日志文件路径
 
analyze_root_cause(log_refs) -> {
    "root_cause": str,
    "evidence": list[str],
}
execution_id 标识一次测试执行。
"""

from langgraph graph import StateGraph 

def llm_node(state MessageState):
    pass 

def run_test(execution_id, case_id):
    pass 
 
def collect_logs(execution_id):
    pass 
# 返回日志文件路径
 
def analyze_root_cause(log_refs):
    pass 


builder = StateGraph(MessageState)
builder.add_node("run_test", run_test)
builder.add_node("collect_logs", collect_logs)
builder.add_node("analyze_root_cause", analyze_root_cause)
builder.add_edge(START, "run_test")

