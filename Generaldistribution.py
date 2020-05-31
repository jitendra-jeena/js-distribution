class Distribution:

    """Generic class for calculating and visualizing probability distributions """
    def __init__(self,mu =0,sigma = 1):

        """Attributes:
                mean(float) stores mean value of the distribution
                stdev(float) stores the standard deviation of the distribution
                data(list) stores list of values extracted from the file
        """
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self,file_name):

        """Function to read data from the file
        Attributes:
                file_name: name of the file  conatining data(text file)

            Returns:
                None
        """
        with open(file_name) as f:
            data_list = []
            line = f.readline()
            while line:
                data_list.append(float(line))
                line = f.readline()
        f.close()
        self.data = data_list