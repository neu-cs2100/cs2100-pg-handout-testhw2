"""
sorting.py
Module responsible for sorting 311 cases and managing urgency rankings.
Combines sorting and urgency functions as they work together conceptually.
"""

import pandas as pd

class CaseSorter:
    """
    Class for sorting and ranking 311 cases.
    """

    def __init__(self) -> None:
        """Initialize CaseSorter, no parameters needed."""
        pass

    def sort_by_days_open(self, df: pd.DataFrame, ascending: bool = False) -> pd.DataFrame:
        """
        Sort the 311 cases by how long they were open.
        
        Args:
            df (pd.DataFrame): The 311 cases dataset
            ascending (bool): If True, sort from shortest to longest duration
            
        Returns:
            pd.DataFrame: Sorted dataset
            
        Raises:
            KeyError: If 'days_open' column doesn't exist
            ValueError: If days_open contains non-numeric values
        """
        pass
    def create_urgency_ranking(self, df: pd.DataFrame) -> dict[str, int]:
        """
        Create an urgency ranking system for 311 case categories.
        
        Args:
            df (pd.DataFrame): The 311 cases dataset
            
        Returns:
            Dict[str, int]: Dictionary mapping categories to urgency scores 
                           (1 = least urgent, higher = more urgent)

            Each category in the dataset is assigned a score which is the 
            number of times it appears in the dataset.

            Example:
            The following output means that 'Traffic Signal Repair' appears 1 time,
            'Street Defects' appears 2 times, etc.
            {
                'Traffic Signal Repair': 1,
                'Street Defects': 2,
                ...
            } 
            
        Raises:
            KeyError: If 'Category' column doesn't exist
        """
        pass

    def filter_data(self, df: pd.DataFrame, urgency_ranking: dict[str, int]) -> pd.DataFrame:
        """
        Filter the dataset to include only the categories that have been ranked 
        (ie. the keys of urgency_ranking).
        
        Args:
            df (pd.DataFrame): The 311 cases dataset
            urgency_ranking (Dict[str, int]): Urgency ranking dictionary
            
        Returns:
            pd.DataFrame: Filtered dataset
            
        Raises:
            ValueError: If urgency_ranking is empty
            ValueError: If no data matches the filter
            KeyError: If 'category' column doesn't exist
        """
        pass

    def sort_by_urgency(self, df: pd.DataFrame, urgency_ranking: dict[str, int]) -> pd.DataFrame:
        """
        Sort 311 cases by urgency ranking.
        
        Args:
            df (pd.DataFrame): The 311 cases dataset
            urgency_ranking (Dict[str, int]): Dictionary mapping categories to urgency scores, 
            higher urgency score is more urgent.

            If multiple cases are in the same category, they are sorted by days_open (descending).
            (Cases that have been open longer are considered more urgent)
            
        Returns:
            pd.DataFrame: Dataset sorted by urgency (most urgent first)
            
        Raises:
            ValueError: If urgency_ranking is empty
            ValueError: If 'days_open' contains non-numeric values
            ValueError: If any category in the dataset is missing from urgency_ranking
            KeyError: If 'category' column doesn't exist
        """
        pass
