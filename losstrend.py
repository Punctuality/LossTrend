import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import clear_output


class LossTrend():
    """

    Class of an object for fine displaying of Loss trend

    """
    def __init__(self, with_test = False):
        sns.set()

        self.with_test = with_test

        self.loss_log = []
    def add_loss(self, cur_loss):
        """

        This method adds a new loss value to the list

        Parameters:
            cur_loss - loss value to add

        Example:
            test = LossTrend()
            test.add_loss(10)

        """
        if self.with_test == True:
            try:             #Train loss             #Test/Val loss
                cur_loss = [float(cur_loss[0]), float(cur_loss[1])]
            except:
                assert False, "Wrong type of loss variable. Should be float convertable"
        else:
            try:             #Train loss             #Test/Val loss
                cur_loss = float(cur_loss)
            except:
                assert False, "Wrong type of loss variable. Should be float convertable"
        self.loss_log.append(cur_loss)

    def plot(self, last_n = -1, epoch = -1, figure_size = (10,6)):

        """

        This method is compiling and plotting the picture of loss trend.

        Parameters:
            last_n - how many last loss values to plot. (-1) if all of them
            epoch - value to print current epoch. (-1) if not to print
            figure_size - sets size of picture to show

        Example:
            test = LossTrend()
            test.add_loss(10)
            test.plot(last_n = 1, epoch = 0, figure_size = (10,8))

        """

        plt.figure(figsize = (10,6))

        plt.axvline(0, c = 'black')
        plt.axhline(0, c = 'black')
        plt.xlabel("Iterations")
        plt.ylabel("Loss value")

        if not last_n == -1:
            to_plot = self.loss_log[-last_n:]
        else:
            to_plot = self.loss_log

        if self.with_test == False:
            tr = [elem for elem in to_plot]
            self.minimum = min(tr)
            plt.axhline(self.minimum, c = 'green')
            plt.plot(range(len(tr)), tr, c = 'red', label = "loss")
            plt.scatter([len(tr)-1], tr[-1], c = 'red')
            plt.legend(loc = 0)
        else:
            tr = [elem[0] for elem in to_plot]
            ts = [elem[1] for elem in to_plot]
            self.minimum = min(ts)
            plt.axhline(self.minimum, c = 'green')
            plt.plot(range(len(tr)), tr, c = 'red', label = "train")
            plt.scatter([len(tr)-1], [tr[-1]], c = 'red')
            plt.plot(range(len(ts)), ts, c = 'blue', label = "test")
            plt.scatter([len(ts)-1], [ts[-1]], c = 'blue')
            plt.legend(loc = 1)

        info_line = ""

        if not epoch == -1:
            info_line += "Epoch: {}".format(epoch+1)
        info_line += " | Minimum Loss: {}".format(self.minimum)
        plt.title(info_line)

        clear_output(True)
        plt.show()

    def process(self, cur_loss, every_n = 10, last_n = -1, epoch = -1):
        """

        This method combines add_loss and plot methods

        Parameters:
            cur_loss - loss value to add
            every_n - value to control frequency of plotting.
                        Picture will be shown on every_n time of adding a value
            last_n - how many last loss values to plot. (-1) if all of them
            epoch - value to print current epoch. (-1) if not to print

        """
        if int(every_n) < 1:
            assert False, "Every_n is less than 1"
        self.add_loss(cur_loss)
        if len(self.loss_log) % int(every_n) == 0:
            self.plot(last_n, epoch)
