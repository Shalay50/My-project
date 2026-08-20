
# Hello Agent - Core Dispatcher, Gates, and Loop definitions
# (Extracted from COSC726 Lab 3)

def gate_2_args_model(args):
    # Args validation logic
    pass

def gate_3_order_id(order_id):
    # Order ID validation logic
    pass

def gate_4_coheres(action):
    # Business logic validation logic
    pass

def gate_5_answer_supported(trace):
    audit_data = audit(trace)
    if not audit_data.get("claim_is_supported", True):
        raise Exception("Gate 5 Error: Final answer not supported by trace.")
