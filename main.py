import numpy as np
from scipy import stats

def main():
    with open('files/cosine_values_for_ttest_generate.txt', 'r', encoding='utf8') as source:
        contents = (source.readlines())
        contents = [float(content.strip()) for content in contents]
        contents = np.array(contents)

    with open('files/cosine_values_for_ttest_original.txt', 'r', encoding='utf8') as source:
        original_contents = (source.readlines())
        original_contents = [float(content.strip()) for content in original_contents]
        original_contents = np.array(original_contents)

    average_x1 = contents.mean()
    average_x2 = original_contents.mean()

    variance_content = contents.var(ddof=1)
    variance_original_content = original_contents.var(ddof=1)

    sd_sd1 = np.sqrt(variance_content)
    sd_sd2 = np.sqrt(variance_original_content)

    n_n1 = len(contents)
    n_n2 = len(original_contents)

    z_value = (average_x1 - average_x2)/np.sqrt((sd_sd1 ** 2 / n_n1) + (sd_sd2 ** 2 / n_n2))
    print('average x1 :: ' + str(average_x1))
    print('average x2 :: ' + str(average_x2))
    print('standard deviation 1 :: ' + str(sd_sd1))
    print('standard deviation 2 :: ' + str(sd_sd2))
    print('z-value :: ' + str(z_value))

if __name__ == '__main__':
    main()
