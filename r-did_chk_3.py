hospitals, first, last, N_reported = 412, 2009, 2019, 4712
years = last - first + 1
print("years:", years)
print("balanced N:", hospitals*years, "| reported:", N_reported, "| equal:", hospitals*years == N_reported)
print("reported N / hospitals:", N_reported/hospitals, "| integer:", N_reported % hospitals == 0)
print("balanced N if 2009 lost to the t-1 peer lag:", hospitals*(years - 1))
print("excess of reported over balanced N:", N_reported - hospitals*years)
