from autowsgr.fight.event.event_2024_0930 import EventFightPlan20240930
from autowsgr.scripts.main import start_script


timer = start_script('./user_settings.yaml')
# set_support(timer,True) # 如果要在战斗前开启战役支援请取消这一行的注释
plan = EventFightPlan20240930(
    timer,
    plan_path='E5ADF',
    fleet_id=4,
)  # 修改E11CD.yaml为相对于的plan，详细的plan名可在data/plans/event/202409309查看，fleet_id为出击编队


plan.run_for_times(
    500,
)  # 第一个参数是战斗次数,还有个可选参数为检查远征时间，默认为1800S
