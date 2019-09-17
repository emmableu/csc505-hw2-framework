/**
 *
 * @author yv
 */
public class Solution {

    /**
     * @param args the command line arguments
     */
    int comparisonCount;
    int[] sortingArray;
    int[] inputArray;

    //public static void main(String[] args)
    //{
    //   instance = Solution();
    //}

    Solution(int[] input)
    {
        inputArray = input;
        comparisonCount = 0;
    }

    public void mergeSort(int p, int r) {
        // TODO
    }

    public void insertionSort() {
    //     sortingArray = new int[inputArray.length];
    //     sortingArray[0] = inputArray[0];
    //     int j = 0;
    //     comparisonCount = 1;
    //     for(int i = 1;i < inputArray.length;i++)
    //     {
    //       for(j=0;j < i;j++)
    //       {
    //          comparisonCount++;
    //          if(sortingArray[j] > inputArray[i])
    //          {
    //             break;
    //          }
    //       }
    //       for(k = i; k > j ;k--)
    //       {
    //          sortingArray[k] = sortingArray[k-1];
    //       }
    //       sortingArray[k] = inputArray[i];
    //     }
    //     for(int i = 0;i< sortingArray.length; i++)
    //     {
    //        System.out.println(sortingArray[i]);
    //     }
    // }
        sortingArray = new int[]{1, 2, 3, 4};
        comparisonCount = 3;

    public  void heapSort()  {
        // TODO
    }

}
