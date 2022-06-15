from element import Element
from exceptions import IncorrectNumberException, ElementNotFoundException
import sqlite3

def _get_element_from_db(number: int) -> Element:
    cur = db_conn.cursor()
    res = cur.execute(f'select * from elements where Number = {number}').fetchone()
    return Element(res[0], (res[1], res[2], res[3]), res[4], bool(res[5]), res[6], res[7], tuple(float(i) for i in res[8].split(' ')), res[9], bool(res[10]), res[11])


if "if для сворачивания":
    db_conn = sqlite3.connect('elements.db')
    H = _get_element_from_db(1)
    He = _get_element_from_db(2)
    Li = _get_element_from_db(3)
    Be = _get_element_from_db(4)
    B = _get_element_from_db(5)
    C = _get_element_from_db(6)
    N = _get_element_from_db(7)
    O = _get_element_from_db(8)
    F = _get_element_from_db(9)
    Ne = _get_element_from_db(10)
    Na = _get_element_from_db(11)
    Mg = _get_element_from_db(12)
    Al = _get_element_from_db(13)
    Si = _get_element_from_db(14)
    P = _get_element_from_db(15)
    S = _get_element_from_db(16)
    Cl = _get_element_from_db(17)
    Ar = _get_element_from_db(18)
    K = _get_element_from_db(19)
    Ca = _get_element_from_db(20)
    Sc = _get_element_from_db(21)
    Ti = _get_element_from_db(22)
    V = _get_element_from_db(23)
    Cr = _get_element_from_db(24)
    Mn = _get_element_from_db(25)
    Fe = _get_element_from_db(26)
    Co = _get_element_from_db(27)
    Ni = _get_element_from_db(28)
    Cu = _get_element_from_db(29)
    Zn = _get_element_from_db(30)
    Ga = _get_element_from_db(31)
    Ge = _get_element_from_db(32)
    As = _get_element_from_db(33)
    Se = _get_element_from_db(34)
    Br = _get_element_from_db(35)
    Kr = _get_element_from_db(36)
    Rb = _get_element_from_db(37)
    Sr = _get_element_from_db(38)
    Y = _get_element_from_db(39)
    Zr = _get_element_from_db(40)
    Nb = _get_element_from_db(41)
    Mo = _get_element_from_db(42)
    Tc = _get_element_from_db(43)
    Ru = _get_element_from_db(44)
    Rh = _get_element_from_db(45)
    Pd = _get_element_from_db(46)
    Ag = _get_element_from_db(47)
    Cd = _get_element_from_db(48)
    In = _get_element_from_db(49)
    Sn = _get_element_from_db(50)
    Sb = _get_element_from_db(51)
    Te = _get_element_from_db(52)
    I = _get_element_from_db(53)
    Xe = _get_element_from_db(54)
    Cs = _get_element_from_db(55)
    Ba = _get_element_from_db(56)
    La = _get_element_from_db(57)
    Ce = _get_element_from_db(58)
    Pr = _get_element_from_db(59)
    Nd = _get_element_from_db(60)
    Pm = _get_element_from_db(61)
    Sm = _get_element_from_db(62)
    Eu = _get_element_from_db(63)
    Gd = _get_element_from_db(64)
    Tb = _get_element_from_db(65)
    Dy = _get_element_from_db(66)
    Ho = _get_element_from_db(67)
    Er = _get_element_from_db(68)
    Tm = _get_element_from_db(69)
    Yb = _get_element_from_db(70)
    Lu = _get_element_from_db(71)
    Hf = _get_element_from_db(72)
    Ta = _get_element_from_db(73)
    W = _get_element_from_db(74)
    Re = _get_element_from_db(75)
    Os = _get_element_from_db(76)
    Ir = _get_element_from_db(77)
    Pt = _get_element_from_db(78)
    Au = _get_element_from_db(79)
    Hg = _get_element_from_db(80)
    Tl = _get_element_from_db(81)
    Pb = _get_element_from_db(82)
    Bi = _get_element_from_db(83)
    Po = _get_element_from_db(84)
    At = _get_element_from_db(85)
    Rn = _get_element_from_db(86)
    Fr = _get_element_from_db(87)
    Ra = _get_element_from_db(88)
    Ac = _get_element_from_db(89)
    Th = _get_element_from_db(90)
    Pa = _get_element_from_db(91)
    U = _get_element_from_db(92)
    Np = _get_element_from_db(93)
    Pu = _get_element_from_db(94)
    Am = _get_element_from_db(95)
    Cm = _get_element_from_db(96)
    Bk = _get_element_from_db(97)
    Cf = _get_element_from_db(98)
    Es = _get_element_from_db(99)
    Fm = _get_element_from_db(100)
    Md = _get_element_from_db(101)
    No = _get_element_from_db(102)
    Lr = _get_element_from_db(103)
    Rf = _get_element_from_db(104)
    Db = _get_element_from_db(105)
    Sg = _get_element_from_db(106)
    Bh = _get_element_from_db(107)
    Hs = _get_element_from_db(108)
    Mt = _get_element_from_db(109)

    Ds = _get_element_from_db(110)
    Rg = _get_element_from_db(111)
    Cn = _get_element_from_db(112)
    Nh = _get_element_from_db(113)
    Fl = _get_element_from_db(114)
    Mc = _get_element_from_db(115)
    Lv = _get_element_from_db(116)
    Ts = _get_element_from_db(117)
    Og = _get_element_from_db(118)



elements_list = [
    H, 
    He, 
    Li, 
    Be, 
    B, 
    C,
    N,
    O,
    F,
    Ne,
    Na,
    Mg,
    Al,
    Si,
    P,
    S,
    Cl,
    Ar,
    K,
    Ca,
    Sc,
    Ti,
    V,
    Cr,
    Mn,
    Fe,
    Co,
    Ni,
    Cu,
    Zn,
    Ga,
    Ge,
    As,
    Se,
    Br,
    Kr,
    Rb,
    Sr,
    Y,
    Zr,
    Nb,
    Mo,
    Tc,
    Ru,
    Rh,
    Pd,
    Ag,
    Cd,
    In,
    Sn,
    Sb,
    Te,
    I,
    Xe,
    Cs,
    Ba,
    La,
    Ce,
    Pr,
    Nd,
    Pm,
    Sm,
    Eu,
    Gd,
    Tb,
    Dy,
    Ho,
    Er,
    Tm,
    Yb,
    Lu,
    Hf,
    Ta,
    W,
    Re,
    Os,
    Ir,
    Pt,
    Au,
    Hg,
    Tl,
    Pb,
    Bi,
    Po,
    At,
    Rn,
    Fr,
    Ra,
    Ac,
    Th,
    Pa,
    U,
    Np,
    Pu,
    Am,
    Cm,
    Bk,
    Cf,
    Es,
    Fm,
    Md,
    No,
    Lr,
    Rf,
    Db,
    Sg,
    Bh,
    Hs,
    Mt,
    Ds,
    Rg,
    Cn,
    Nh,
    Fl,
    Mc,
    Lv,
    Ts,
    Og,
] 

def from_number(num: int) -> Element:
    if num < 1 or num > 118:
        raise IncorrectNumberException(num)
    return elements_list[num - 1]


def from_label(lbl: str) -> Element:
    for i in elements_list:
        if i.label == lbl:
            return i
    raise ElementNotFoundException(f'Label = {lbl}')
            

__all__ = [
    'from_number',
    'from_label',
    'H',
    'He',
    'Li',
    'Be',
    'B',
    'C',
    'N',
    'O',
    'F',
    'Ne',
    'Na',
    'Mg',
    'Al',
    'Si',
    'P',
    'S',
    'Cl',
    'Ar',
    'K',
    'Ca',
    'Sc',
    'Ti',
    'V',
    'Cr',
    'Mn',
    'Fe',
    'Co',
    'Ni',
    'Cu',
    'Zn',
    'Ga',
    'Ge',
    'As',
    'Se',
    'Br',
    'Kr',
    'Rb',
    'Sr',
    'Y',
    'Zr',
    'Nb',
    'Mo',
    'Tc',
    'Ru',
    'Rh',
    'Pd',
    'Ag',
    'Cd',
    'In',
    'Sn',
    'Sb',
    'Te',
    'I',
    'Xe',
    'Cs',
    'Ba',
    'La',
    'Ce',
    'Pr',
    'Nd',
    'Pm',
    'Sm',
    'Eu',
    'Gd',
    'Tb',
    'Dy',
    'Ho',
    'Er',
    'Tm',
    'Yb',
    'Lu',
    'Hf',
    'Ta',
    'W',
    'Re',
    'Os',
    'Ir',
    'Pt',
    'Au',
    'Hg',
    'Tl',
    'Pb',
    'Bi',
    'Po',
    'At',
    'Rn',
    'Fr',
    'Ra',
    'Ac',
    'Th',
    'Pa',
    'U',
    'Np',
    'Pu',
    'Am',
    'Cm',
    'Bk',
    'Cf',
    'Es',
    'Fm',
    'Md',
    'No',
    'Lr',
    'Rf',
    'Db',
    'Sg',
    'Bh',
    'Hs',
    'Mt',
    'Ds',
    'Rg',
    'Cn',
    'Nh',
    'Fl',
    'Mc',
    'Lv',
    'Ts',
    'Og',

]