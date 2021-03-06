"""
The :mod:`sklearn.feature_selection` module implements feature selection
algorithms. It currently includes univariate filter selection methods and the
recursive feature elimination algorithm.
"""

from .univariate_selection import chi2
from .univariate_selection import f_classif
from .univariate_selection import f_oneway
from .univariate_selection import f_regression
from .univariate_selection import SelectPercentile
from .univariate_selection import SelectKBest
from .univariate_selection import SelectFpr
from .univariate_selection import SelectFdr
from .univariate_selection import SelectFwe
from .univariate_selection import GenericUnivariateSelect

from .variance_threshold import VarianceThreshold

from .from_model import SelectFromModel

__all__ = ['GenericUnivariateSelect',
           'SelectFdr',
           'SelectFpr',
           'SelectFwe',
           'SelectKBest',
           'SelectFromModel',
           'SelectPercentile',
           'VarianceThreshold',
           'chi2',
           'f_classif',
           'f_oneway',
           'f_regression']
