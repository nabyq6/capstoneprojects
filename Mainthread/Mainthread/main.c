//********************************************************
//***************this code is down for now****************
//********************************************************
//  main.c
//  Mainthread
//
//  Created by Nicholas Bouckaert on 3/16/19.
//  Copyright © 2019 Nicholas Bouckaert. All rights reserved.
//

#include <stdio.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sched.h>
#include <fcntl.h>
#include <stdint.h>
#include <sys/time.h>
#include <pthread.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <string.h>
// included and works only on the pi
#include <semaphore.h>
#include <wiringPi.h>

#define control_file "control_file.txt"
#define H HIGH 
#define L LOW
#define Zero  26
#define One  27



void write_camera_info_to_file( int needed_camera);
void lets_read_these_pins(); 




int main(int argc, const char * argv[]) {
   
 
    int needed_camera;
    int zero; 
    int one; 

	//setting up to read input from the ardunio 
	wiringPiSetup();
	pinMode(Zero, INPUT);
	pinMode(One, INPUT);
	pinMode(33, OUTPUT);
	pullUpDnControl(Zero, PUD_DOWN);
	pullUpDnControl(One, PUD_DOWN);
	
    while(1)
    {
	digitalWrite(33, H);
	sleep(2);	
	zero = digitalRead(Zero);
	one = digitalRead(One);
	printf("zero is: %d, one is %d\n", zero, one);

	//for left
	if( zero == 1 && one == 1)
		{
		write_camera_info_to_file(2);
		}	

	//for right
	if( zero == 0 && one == 0)
		{
		write_camera_info_to_file(2);
		}	
	
	//for front Camera 
	if( zero == 0 && one == 1)
		{
		write_camera_info_to_file(1);
		}

	// no camera door not open
	if( zero == 1 && one == 0)
		{
		write_camera_info_to_file(0);
		}
       // printf("\nWhat camera would you like to switch it too: ");
        //scanf("%d", &needed_camera);
//        write_camera_info_to_file(needed_camera);
        printf("write was successful\n");
    }
    
    return 0;
}

void write_camera_info_to_file( int needed_camera){
    FILE * camera_file;
    camera_file = fopen(control_file, "w");
    printf("camera: %d", needed_camera);
    fprintf(camera_file, "%d", needed_camera);
    
    fclose(camera_file);
    
}



