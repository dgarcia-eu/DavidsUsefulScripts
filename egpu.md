How to get an external GPU (Nvidia GeForce GTX 1080 in an Akitio Node case) on Thunderbolt running on Ubuntu 19.04:

* Disable SecureBoot in BIOS (maybe necessary)

* Disable Thunderbolt security (definitely necessary!)

* Install the graphic card drivers
      
      #Add repository
      
      sudo add-apt-repository ppa:graphics-drivers/ppa

      #Install build tools
      
      sudo apt-get install dkms build-essential

      sudo apt-get update
      
      #Install latest driver, you can see which are available by writing
      #"sudo apt-get install nvidia-driver-" and pressing TAB
      
      sudo apt-get install nvidia-driver-440

      #After the driver install go ahead and reboot.
      
      sudo shutdown -r Now


* Install docker: https://docs.docker.com/install/linux/docker-ce/ubuntu/

* Post-installation steps for docker
       
      #Create the docker group
      
      sudo groupadd docker
      
      #Add your user to the docker group
      
      sudo usermod -aG docker $USER
      
      #Restart
      
      reboot
      
      #Verify that you can run docker commands without sudo
      
      docker run hello-world


* Install nvidia docker support: https://github.com/NVIDIA/nvidia-docker

* Verify

      #Check if a GPU is available:

      lspci | grep -i nvidia

      #Verify your nvidia-docker installation:

      docker run --gpus all --rm nvidia/cuda nvidia-smi


* Run (or first time install) tensorflow with gpu support:

      docker run --gpus all -it --rm tensorflow/tensorflow:latest-gpu 

Sources:

* https://www.pugetsystems.com/labs/hpc/How-To-Install-CUDA-10-1-on-Ubuntu-19-04-1405/#Step2)GettheNVIDIAdriverinstalled
* https://josehoras.github.io/tensorflow-with-gpu-using-docker-and-pycharm/
