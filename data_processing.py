def process(area, par1=1):
    try:
        area = float(area)
    except:
        area = 0

    res = area * par1
    return res



