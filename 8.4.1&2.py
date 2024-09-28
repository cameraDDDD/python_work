def print_models(unprinted_designs,completed_models):
    """模拟打印每个设计"""
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f"Print model:{current_design}")
        completed_models.append(current_design)
def show_completedmodels(completed_models):
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)
unprinted=['mydick','woruls','strww']
completed_models=[]
print_models(unprinted[:],completed_models)#调用函数修改副本
show_completedmodels(completed_models)
print(unprinted)