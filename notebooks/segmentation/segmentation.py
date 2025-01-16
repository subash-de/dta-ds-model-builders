from headroom_pckg.libs.segmentation import seg_file,default_joins,seg_list_acc


# COMMAND ----------

def driver_acc():
    print(seg_file())
    print(seg_list_acc())

def driver_task():
    print(seg_file())
    print(default_joins())



parameter='task'   # will come as parameter
caller_fun_list={'task':driver_task,'acc':driver_acc}
# COMMAND ----------
caller_fun_list[f'{parameter}']()


