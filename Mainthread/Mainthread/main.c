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

#define control_file "control_file.txt"

void write_camera_info_to_file( int needed_camera);



int main(int argc, const char * argv[]) {
    
    int needed_camera;
    
    while(1)
    {
        printf("\nWhat camera would you like to switch it too: ");
        scanf("%d", &needed_camera);
        write_camera_info_to_file(needed_camera);
        printf("write was successful\n");
    }
    
    return 0;
}

void write_camera_info_to_file( int needed_camera){
    FILE * camera_file;
    camera_file = fopen(control_file, "w");
    
    fprintf(camera_file, "%d", needed_camera);
    
    fclose(camera_file);
    
}



