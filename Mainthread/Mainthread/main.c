//
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
// included and works only on the pi
#include <semaphore.h>

void camera_information( int camera);

int main(int argc, const char * argv[]) {
    
    int camera;
    
    printf("What camera would you like to switch it too: ");
    scanf("%d", &camera );
    
    camera_information(camera);
}

void camera_information( int camera)
{
    //goals is to have this progarm communicate with the python script and have it change cameras based on what LEE sends me
    
    int camera_information;
    int camera_needed = camera;
    
    printf("Reading from the button press setup\n");
    
    if((camera_information = open("Camera_Switch", O_WRONLY)) < 0)
    {
        printf("error opening pipe in camera_information used for scene switching\n");
        exit(-1);
    }
    
   // while (1) shouldnt need while loop for this application
    {
        if( write(camera_information, &camera_needed, sizeof(camera_needed)) < 0)
        {
            printf("Error writing the information for between processes communication\n");
            exit(-1);
        }
        
        printf("reading camera_information transfer occured occured\n");
    }
    
}


