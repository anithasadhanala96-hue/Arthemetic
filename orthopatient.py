orthoamount=2000
import sys
patientage=int(sys.argv[1])
usedamount=int(sys.argv[2])
if(orthoamount):
    if(usedamount<orthoamount and usedamount!=orthoamount):
       if(patientage<=19):
         print("patient eligble for ortho service ")
       else:
            print(f"patient not eligible due to patient age {patientage} but patient used {usedamount:.2f}" )
    elif(patientage<=19):   
          print(f"patient age {patientage}is eligible but used complete {orthoamount:.2f}")
    else:
        print( f"patient used complete {orthoamount:.2f}& also not eligible due to patient age{patientage}" )
else:
    pass       