# Python wrapper for opscale.R
import rpy2.robjects
import os


class OpScale:
    def __init__(self):
        self.r = rpy2.robjects.r
        self.r.source('%s%sopscale.R' % (os.path.dirname(
            __file__), os.path.sep))

    def opscale(self, qual, quant=None, level=1, process=1, na_impute=False,
                na_assign=False, rescale=True):
        """

        :param qual: A vector of data values, assumed nominal or
                   ordinal level measurement
        :param quant: A vector of quantitative values, probably
                   obtained as model estimates
        :param level: Measurement level of qualitative vector, with
                   1 = nominal and 2 = ordinal
        :param process: Measurement process of qualitative vector, with
                   1 = discrete and 2 = continuous
        :param na_impute: FALSE (default) = leave missing values in qualitative
                   vector as missing in optimally scaled vector,
                   TRUE = assign quantitative vector values to
                   optimally scaled vector for missing entries in
                   qualitative vector
        :param na_assign: TRUE (default) = if quantitative value is missing,
                   assign mean of optimally scaled values for the corresponding
                   qualitative value to the optimally scaled vector,
                   FALSE = if quantitative value is missing, leave optimally
                   scaled value missing, even if qualitative value is present
        :param rescale:TRUE (default) = rescale optimally scaled values to the
                   same mean and standard deviation as the values in the
                   original qualitative vector.  FALSE = do not rescale
                   optimally scaled vector
        :return: Optimally scaled version of the qualitative vector
        """

        if not quant:
            quant = list(range(1, len(qual)))

        return list(self.r.opscale(rpy2.robjects.IntVector(qual),
                                   rpy2.robjects.FloatVector(quant),
                                   level, process, na_impute,  na_assign,
                                   rescale).rx2('os'))
