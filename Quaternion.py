import numpy as np
import math as m


def scalar_multiply(base, basement):
    b = np.array(base) * np.array(basement)
    value = 0
    for i in b:
        value = value + float(i)
    return value


class quaternion:
    scalar = 0.0
    basement = np.array([0, 0, 0])

    def __init__(self, value, basement):
        self.basement = basement
        self.scalar = value

    def set_quaternion(self, a, b, c, d):
        self.scalar = a
        self.basement = [b, c, d]
        return self

    def __str__(self):
        print(self.scalar, end='' + '[')
        for i in self.basement:
            print(i, end=' ')
        print(']')
        return ''

    pass


def sum_q(quaternion_this, quaternion_that):
    value = quaternion_this.scalar + quaternion_that.scalar
    base = np.array(quaternion_this.basement) + np.array(quaternion_that.basement)
    quat_a = quaternion(value, base)
    return quat_a


def multiply_scalar(quaternion_this, value):
    val = value * quaternion_this.scalar
    base = np.array(quaternion_this.basement * value)
    quat_a = quaternion(val, base)
    return quat_a


def multiply_quaternion(quaternion_this, quaternion_that):
    value = quaternion_this.scalar * quaternion_that.scalar - scalar_multiply(quaternion_this.basement,
                                                                              quaternion_that.basement)
    base = quaternion_that.scalar * np.array(quaternion_this.basement) + quaternion_this.scalar * np.array(
        quaternion_that.basement) + np.array(np.cross(quaternion_this.basement, quaternion_that.basement))
    quat_a = quaternion(value, base)
    return quat_a


def make_trig(quater):
    quat = multiply_scalar(quater, 1 / norm_quater(quater))
    alpha = 2 * m.acos(quat.scalar)
    rot = np.array(quat.basement) * m.sqrt(norm_quater(quat) ** 2 - quat.scalar ** 2) / norm_quater(quat)
    trig_quater = quaternion(alpha, rot)
    return trig_quater


def a_make_trig(quater):
    scalar = m.cos(quater.scalar / 2)
    base = np.array(quater.basement) / m.sin(quater.scalar / 2)
    q = quaternion(scalar, base)
    return q


def make_conjugated(quater):
    base = np.array((-1) * np.array(quater.basement))
    value = quater.scalar
    q = quaternion(value, base)
    return q


def norm_quater(quater):
    value = multiply_quaternion(quater, make_conjugated(quater))
    value = value.scalar
    value = m.sqrt(value)
    return value


def reverse_quater(quater):
    q1 = make_conjugated(quater)
    value = norm_quater(q1)
    value = 1 / value
    q1 = multiply_scalar(q1, value)
    return q1


def make_one_quater(quater):
    quat = multiply_scalar(quater, 1 / norm_quater(quater))
    return quat


def Euler_to_Quaternion(yaw, pitch, roll):
    q1 = np.sin(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) - np.cos(roll / 2) * np.sin(pitch / 2) * np.sin(yaw / 2)
    q2 = np.sin(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) - np.cos(roll / 2) * np.sin(pitch / 2) * np.sin(yaw / 2)
    q3 = np.cos(roll / 2) * np.cos(pitch / 2) * np.sin(yaw / 2) - np.sin(roll / 2) * np.sin(pitch / 2) * np.cos(yaw / 2)
    q4 = np.cos(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) + np.sin(roll / 2) * np.sin(pitch / 2) * np.sin(yaw / 2)
    base = np.array([q1, q2, q3])
    quat = quaternion(q4, base)
    return quat


def quat_to_string(quat):
    str1 = " "
    str1 += str(float(quat.scalar)) + "["
    for i in quat.basement:
        str1 += str(float(i)) + " "
    str1 += "]"
    return str1
