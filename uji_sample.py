def sample_needed(z,p,m):
 s =(z**2)*(p)*(1-p) / (m**2)
 return s

# s = sample yang dibutuhkan
# z = z score berdasarkan confidence level
# p = population propotion
# m = margin off error
# https://www.youtube.com/watch?v=51NS0cGjBIk

z_score = 		0.17  #confidence level 75% 2 arah
population =50/100
margin =  5/100
print(sample_needed(z_score,population,margin))