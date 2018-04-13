import numpy as np
from scipy import stats

def main():
    with open('files/generate_for_ttest.txt', 'r', encoding='utf8') as source:
        contents = (source.readlines())
        contents = [float(content.strip()) for content in contents]
        contents = np.array(contents)

    with open('files/original_for_ttest.txt', 'r', encoding='utf8') as source:
        original_contents = (source.readlines())
        original_contents = [float(content.strip()) for content in original_contents]
        original_contents = np.array(original_contents)

    average_x1 = contents.mean()
    average_x2 = original_contents.mean()

    sd_sd1 = np.std(contents)
    sd_sd2 = np.std(original_contents)

    n_n1 = len(contents)
    n_n2 = len(original_contents)

    z_value = (average_x1 - average_x2)/np.sqrt((sd_sd1 ** 2 / n_n1) + (sd_sd2 ** 2 / n_n2))
    print('average x1 :: ' + str(average_x1))
    print('average x2 :: ' + str(average_x2))
    print('standard deviation 1 :: ' + str(sd_sd1))
    print('standard deviation 2 :: ' + str(sd_sd2))
    print('members 1 :: ' + str(n_n1))
    print('members 2 :: ' + str(n_n2))
    print('z-value :: ' + str(z_value))

if __name__ == '__main__':
    main()
