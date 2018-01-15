#include <stdio.h>
#include <dirent.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, const char *argv[])
{
	char name[20] = {0};
	printf("Please enter name of bike stop: ");
	scanf("%s", name);
	DIR* proc_dir;
	FILE* proc = NULL, *output;
	char filename[100]={0};
	proc_dir = opendir(".");
	struct dirent* proc_content;
	char content[1000]={0};
	int num = 0;
	output = fopen("raw_data", "w+");
	char line[100];
	while((proc_content = readdir(proc_dir)) != NULL) {
		if(strcmp(proc_content->d_name,"..") && strcmp(proc_content->d_name,".") && strcmp(proc_content->d_name,"a.out") && strcmp(proc_content->d_name, "raw_data") && strcmp(proc_content->d_name, "pre.py") && strcmp(proc_content->d_name, "probability.py") && strcmp(proc_content->d_name, "par.c") && strcmp(proc_content->d_name, "makefile"))
		{
			memset(filename, '\0', sizeof(filename));
			sprintf(filename, "%s", proc_content->d_name);
			proc = fopen(filename, "r");
			//printf("%s\n", proc_content->d_name);
			while(!feof(proc))
			{
				memset(content, '\0', sizeof(content));
				fscanf(proc, "%s", content);
				if(strstr(content, name) != NULL)
				{
					//printf("%s\n", content);
					fprintf(output, "%s\n", content);
				}
			}
			fclose(proc);
		}
	}	
	closedir(proc_dir);
	fclose(output);
	return 0;
}
