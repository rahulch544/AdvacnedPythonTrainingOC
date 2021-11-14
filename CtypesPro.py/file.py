# apelix@krosumlabs:~/D1$ cat p1.c
# int add_total(int a,int b){
# 	return a+b;
# }
# apelix@krosumlabs:~/D1$ cat p2.c
# int add_count(int a){
# 	return a+100;
# }
# apelix@krosumlabs:~/D1$ cat p3.c
# float mul_float(float a,float b){
# 	return a*b;
# }
# gcc -c p1.c
# gcc -c p2.c
# LVCInstructor to Everyone (3:17 PM)
# gcc -c p3.c
# gcc -shared p1.o p2.o p3.o -o libmycfile.so
import ctypes
pv=ctypes.CDLL("./libmycfile.so")
print(pv.add_total(10,20))
print(pv.add_count(120))


http://aru.us.oracle.com/rest/cpm/series/openRelease?series_name=WebCenter%20Core%20Bundle%20Patch%2012.2.1.5.0&label_name=WCCORE_12.2.1.5.0WCCOREBP_GENERIC_210812.2003
