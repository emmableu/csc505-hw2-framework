import org.junit.Test;
import org.junit.Assert;


/**
 *
 * @author yv
 */
public class SortingTest {

    /**
     * Test of mergeSort method, of class Sorting.
     */
    @Test
    public void testMergeSort() {
        System.out.println("Testing mergeSort...\n");
        int[] nums1 = new int[]{ 3, 6, 1 };
        int[] expResult1 = new int[]{ 1, 3, 6 };
        Solution instance = new Solution(nums1);
        instance.mergeSort(0, nums1.length-1);
        Assert.assertArrayEquals(expResult1, instance.sortingArray);
        Assert.assertEquals(5, instance.comparisonCount);

        int[] nums2 = new int[]{ 7, 3, 1, 5, 6, 2, 4 };
        int[] expResult2 = new int[]{ 1, 2, 3, 4, 5, 6, 7 };
        instance = new Solution(nums2);
        instance.mergeSort(0, nums2.length-1);
        Assert.assertArrayEquals(expResult2, instance.sortingArray);
        Assert.assertEquals(20, instance.comparisonCount);
    }

    /**
     * Test of insertionSort method, of class Sorting.
     */
    @Test
    public void testInsertionSort() {
        System.out.println("Testing mergeSort...\n");
        int[] nums1 = new int[]{ 3, 6, 1 };
        int[] expResult1 = new int[]{ 1, 3, 6 };
        Solution instance = new Solution(nums1);
        instance.insertionSort();
        Assert.assertArrayEquals(expResult1, instance.sortingArray);
        Assert.assertEquals(3, instance.comparisonCount);

        int[] nums2 = new int[]{ 7, 3, 1, 5, 6, 2, 4 };
        int[] expResult2 = new int[]{ 1, 2, 3, 4, 5, 6, 7 };
        instance = new Solution(nums2);
        instance.insertionSort();
        Assert.assertArrayEquals(expResult2, instance.sortingArray);
        Assert.assertEquals(16, instance.comparisonCount);
    }

    /**
     * Test of heapSort method, of class Sorting.
     */
    @Test
    public void testHeapSort() {
        System.out.println("Testing heapSort...\n");
        int[] nums1 = new int[]{ 3, 6, 1 };
        int[] expResult1 = new int[]{ 1, 3, 6 };
        Solution instance = new Solution(nums1);
        instance.heapSort();
        Assert.assertArrayEquals(expResult1, instance.sortingArray);
        Assert.assertEquals(3, instance.comparisonCount);

        int[] nums2 = new int[]{ 7, 3, 1, 5, 6, 2, 4 };
        int[] expResult2 = new int[]{ 1, 2, 3, 4, 5, 6, 7 };
        instance = new Solution(nums2);
        instance.heapSort();
        Assert.assertArrayEquals(expResult2, instance.sortingArray);
        Assert.assertEquals(17, instance.comparisonCount);

    }

}
