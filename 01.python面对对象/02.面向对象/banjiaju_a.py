# encoding:utf-8


class Furnitur():

    def __init__(self, name, area):
        # 家具名称
        self.name = name
        # 家具占用面积
        self.area = area


class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 占地面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具面积
        self.furnitur = []

    def add_furnitur(self, item):
        # 容纳家具
        # 如果家具占地面积<=房子剩余面积，就可以搬入
        # if item.area <= self.free_area:
        #     print("现在添加的家具是%s" % item.name)
        #     # 房屋剩余面积-该家具的占地面积
        #     self.furnitur.append(item.name)
        #     self.free_area -= item.area
        # # 否则：提示用户家具太大不能搬入
        # else:
        #     print("家具太大，不能搬入")

        self.furnitur.append(item.name)
        print(self.furnitur)


    def __str__(self):
        return f"房子地理位置在{self.address},房屋的面积是{self.area},房子的剩余面积{self.free_area},房子的家具有{self.furnitur}"


# 双人床

bed = Furnitur('双人床', 6)
sofa = Furnitur('沙发', 10)

# 房子1：北京，1000
jia1 = Home('北京', 1000)
print(jia1)

jia1.add_furnitur(bed)
print(jia1)
