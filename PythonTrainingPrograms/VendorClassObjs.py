import vendorClass

v1 = vendorClass.vendor("Rahul","IBM","GST-1234")
v1.billing('P1',1000)
v2 = vendorClass.vendor("Raj","AX","GST-456")
v2.billing('P2',1000)
v1.billing('P1',1033)
v1.billing('P2',1330)