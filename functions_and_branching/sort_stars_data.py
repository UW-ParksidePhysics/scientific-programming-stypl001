import math as m

# Table is set to have 1) Name of Star 2) Distance from Sun in light years 3) Apparent brightness 4) The luminosity.

class Star():
    def __init__(self, name, distance, brightness, luminosity):
      self.name = name
      self.distance = distance
      self.brightness = brightness
      self.luminosity = luminosity

    def __repr__(self):
      return '({},{},{},{})'.format(self.name, self.distance, self.brightness, self.luminosity)


s1 = Star('Alpha Centauri A',     4.3,   0.26,       1.56)
s2 = Star('Alpha Centauri B',     4.3,   0.077,      0.45)
s3 = Star('Alpha Centauri C',     4.2,   0.00001,    0.00006)
s4 = Star('Barnards Star',        6.0,   0.00004,    0.0005)
s5 = Star('Wolf 359',             7.7,   0.000001,   0.00002)
s6 = Star('BD + 36 degrees 2147', 8.2,   0.00003,    0.006)
s7 = Star('Luyten 726-8 A',       8.4,   0.000003,   0.00006)
s8 = Star('Luyten 726-8 B',       8.4,   0.000002,   0.00004)
s9 = Star('Sirius A',             8.6,   1.00,       23.6)
s10 = Star('Sirius B',             8.6,   0.001,      0.003)
s11 = Star('Ross 154',             9.4,   0.00002,    0.0005)

star = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]

def s_sort(sta):
  return sta.distance

s_stars = sorted(star, key=s_sort)
print(s_stars)

def s_sort(sta):
  return sta.brightness

s_stars = sorted(star, key=s_sort)
print(s_stars)

def s_sort(sta):
  return sta.luminosity

s_stars = sorted(star, key=s_sort)
print(s_stars)
