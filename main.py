import numpy as np
from scipy import stats

def main():
    with open('files/cosine_values_for_ttest_generate.txt', 'r', encoding='utf8') as source:
        contents = (source.readlines())
        contents = [float(content.strip()) for content in contents]
        contents = np.array(contents)
        # print(contents.mean())

    with open('files/cosine_values_for_ttest_original.txt', 'r', encoding='utf8') as source:
        original_contents = (source.readlines())
        original_contents = [float(content.strip()) for content in original_contents]
        original_contents = np.array(original_contents)
        # print(original_contents.mean())

    # Sample Size
    N = 100
    # ddof = dynamic degree of freedom
    variance_of_contents = contents.var(ddof=1)
    variance_of_original_contents = original_contents.var(ddof=1)

    print(variance_of_contents)
    print(variance_of_original_contents)

    # std deviation
    sd = np.sqrt((variance_of_contents + variance_of_original_contents)/2)
    print(sd)

    # Calculate the t-statistics
    t_stats = (contents.mean() - original_contents.mean())/(sd*np.sqrt(2/N))

    # Compare with the critical t-value
    df = 2*N - 2
    # p-value after comparison with the t
    p_value = 1 - stats.t.cdf(t_stats, df=df)

    print(t_stats)
    # print(p_value)
    #
    #
    # print("t = " + str(t))
    # print("p = " + str(2*p))
    # #Note that we multiply the p value by 2 because its a twp tail t-test
    # ### You can see that after comparing the t statistic with the critical t value (computed internally) we get a good p value of 0.0005 and thus we reject the null hypothesis and thus it proves that the mean of the two distributions are different and statistically significant.
    #
    #
    # ## Cross Checking with the internal scipy function
    # t2, p2 = stats.ttest_ind(a,b)
    # print("t = " + str(t2))
    # print("p = " + str(2*p2))

if __name__ == '__main__':
    main()
