
class CarHistory:
    def __init__(self, original_car_id, car_id, car_spec, car_used, num_changed, emergency_accident, my_car_damage, other_car_damage):
        self.original_car_id = original_car_id
        self.car_id = car_id
        self.car_spec = car_spec
        self.car_used = False if car_used == "없음" else True
        self.num_changed = num_changed
        self.emergency_accident = emergency_accident
        self.my_car_damage = my_car_damage
        self.other_car_damage = other_car_damage
        # 자동차 번호, 소유자 변경 횟수 구분
        num_changed_detail = num_changed.split("/")
        num_changed_detail[1] = num_changed_detail[1].replace(" ", "")
        self.car_num_changed = int(num_changed_detail[0][0])
        self.car_owner_changed = int(num_changed_detail[1][0])


    def __str__(self):
        return 'CarHistory(original_car_id=' + str(self.original_car_id) + ", car_id=" + str(self.car_id) \
            + ', car_spec=' + str(self.car_spec) + ', car_used=' + str(self.car_used) + ', num_changed=' + \
            str(self.num_changed) + ', emergency_accident=' + str(self.emergency_accident) + ', my_car_damage=' \
            + str(self.my_car_damage) + ', other_car_damage=' + str(self.other_car_damage)