N = int(raw_input())
vert_up_len = N
vert_down_len = N -1
hort_tot_len = (2 * (N + (N -1))) - 1 
vert_tot_len = vert_up_len + vert_down_len
alpha_list = 'abcdefghijklmnopqrstuvwxyz'
vert_counter = 0
alpha_counter = N - 1
j = hort_tot_len / 2
tmp_str_l= alpha_list[alpha_counter]
tmp_var_l = alpha_counter
tmp_str_r=alpha_list[alpha_counter - 1]
tmp_var_r= alpha_counter - 1

while vert_counter < vert_up_len:
	#print 'vert_counter:' + str(vert_counter)
	if vert_counter == 0:
		print '-'* (hort_tot_len/2) + alpha_list[alpha_counter] + '-' * (hort_tot_len/2)
	else:
		j = j - 2
		tmp_str_l = tmp_str_l + '-' + alpha_list[tmp_var_l]
		tmp_str_r = '-' + tmp_str_r + '-' + alpha_list[tmp_var_r + 1]
		print '-' * j + tmp_str_l + tmp_str_r + '-' * j


		
	vert_counter = vert_counter + 1
	tmp_var_l = tmp_var_l - 1 
 
