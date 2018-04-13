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

    variance_content = contents.var(ddof=1)
    variance_original_content = original_contents.var(ddof=1)

    sd_sd1 = np.sqrt(variance_content)
    sd_sd2 = np.sqrt(variance_original_content)

    n_n1 = len(contents)
    n_n2 = len(original_contents)

    t_value = (average_x1 - average_x2)/np.sqrt((sd_sd1 ** 2 / n_n1) + (sd_sd2 ** 2 / n_n2))
    # df = (n_n1 + n_n2) - 2
    df = 58
    p_value = 1 - stats.t.cdf(t_value, df=df)
    print('average x1 :: ' + str(average_x1))
    print('average x2 :: ' + str(average_x2))
    print('standard deviation 1 :: ' + str(sd_sd1))
    print('standard deviation 2 :: ' + str(sd_sd2))
    print('members 1 :: ' + str(n_n1))
    print('members 2 :: ' + str(n_n2))
    print('t-value :: ' + str(t_value))
    print('p-value :: ' + str(p_value))


    ## Cross Checking with the internal scipy function
    t2, p2 = stats.ttest_ind(original_contents, contents)
    print("t = " + str(t2))
    print("p = " + str(2*p2))


if __name__ == '__main__':
    main()
