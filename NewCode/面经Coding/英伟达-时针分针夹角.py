"""
Q1: 根据时间字符串计算时针与分针之间的最小夹角。
思路：分别计算时针和分针相对于12点方向的角度。分针角度 = 分钟 × 6°，时针角度 = 小时 × 30° + 分钟 × 0.5°。计算两角度差的绝对值，若超过180°则用360°减去该值。时间复杂度O(1)。

作者：Quill_79
链接：https://www.nowcoder.com/feed/main/detail/72ae742499bc4460bc9c3c71c705f38b?sourceSSR=search
来源：牛客网
"""

def clock_angle(time: str) -> float:
    hh, mm = map(int, time.split(":"))
    h = hh % 12
    angle_h = h * 30 + mm * 0.5
    angle_m = mm * 6
    diff = abs(angle_h - angle_m)
    return min(diff, 360 - diff)

if __name__ == "__main__":
    print(clock_angle("12:00"))
    print(clock_angle("03:00"))
    print(clock_angle("06:00"))
    print(clock_angle("01:05"))
