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

    average_x1 = round(contents.mean(), 4)
    average_x2 = round(original_contents.mean(), 4)

    sd_sd1 = round(np.std(contents), 4)
    sd_sd2 = round(np.std(original_contents), 4)

    v_1 = round(sd_sd1 ** 2, 4)
    v_2 = round(sd_sd2 ** 2, 4)

    n_n1 = len(contents)
    n_n2 = len(original_contents)

    divider = round(np.sqrt((v_1 + v_2)/100), 4)


    dividey = round((average_x1 - average_x2), 4)
    print('average x1 :: ' + str(average_x1))
    print('average x2 :: ' + str(average_x2))
    print('standard deviation 1 :: ' + str(sd_sd1))
    print('standard deviation 2 :: ' + str(sd_sd2))
    print('variance 1 :: ' + str(v_1))
    print('variance 2 :: ' + str(v_2))
    # print('members 1 :: ' + str(n_n1))
    # print('members 2 :: ' + str(n_n2))
    print('z-value :: ' + str(round((dividey/divider), 2)))

if __name__ == '__main__':
    main()
