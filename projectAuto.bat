echo RUNNING PROJECT MULTISPECTRAL
"C:\Program Files\Pix4Dmapper\pix4dmapper" -c -n --image-dir "thetford-site1-20180713-multispectral" --template TELUQgeneral "C:\Users\zdeziel\Documents\TELUQ\missions\thetford-20180713\thetford-site1-20180713-multispectral.p4d"
echo PROCESSING FINISHED

echo RUNNING PROJECT RGB
"C:\Program Files\Pix4Dmapper\pix4dmapper" -c -n --image-dir "thetford-site1-20180713-rgb" --template TELUQgeneral "C:\Users\zdeziel\Documents\TELUQ\missions\thetford-20180713\thetford-site1-20180713-rgb.p4d"
echo PROCESSING FINISHED

echo RUNNING INITIAL PROCESSING THERMAL
"C:\Program Files\Pix4Dmapper\pix4dmapper" -c --cam-param-project -i --image-dir "thetford-site1-20180713-thermal" --template TELUQgeneral "C:\Users\zdeziel\Documents\TELUQ\missions\thetford-20180713\thetford-site1-20180713-thermal.p4d"
echo INITIAL PROCESSING FINISHED

echo RUNNING PROJECT MULTISPECTRAL
"C:\Program Files\Pix4Dmapper\pix4dmapper" -c -n --image-dir "thetford-site2-20180713-multispectral" --template TELUQgeneral "C:\Users\zdeziel\Documents\TELUQ\missions\thetford-20180713\thetford-site2-20180713-multispectral.p4d"
echo PROCESSING FINISHED

echo RUNNING PROJECT RGB
"C:\Program Files\Pix4Dmapper\pix4dmapper" -c -n --image-dir "thetford-site2-20180713-rgb" --template TELUQgeneral "C:\Users\zdeziel\Documents\TELUQ\missions\thetford-20180713\thetford-site2-20180713-rgb.p4d"
echo PROCESSING FINISHED

echo RUNNING INITIAL PROCESSING THERMAL
"C:\Program Files\Pix4Dmapper\pix4dmapper" -c --cam-param-project -i --image-dir "thetford-site2-20180713-thermal" --template TELUQgeneral "C:\Users\zdeziel\Documents\TELUQ\missions\thetford-20180713\thetford-site2-20180713-thermal.p4d"
echo INITIAL PROCESSING FINISHED

