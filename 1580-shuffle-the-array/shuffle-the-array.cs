public class Solution {
    public int[] Shuffle(int[] nums, int n) {
        int[] a = new int[2*n];
        int b = n;
        int c=0;
        for (int i=0; i<2*n; i++)
        {
            if (i % 2 == 1)
            {
                a[i] = nums[b];
                b=b+1;
            }
            else
            {
                a[i] = nums[c];
                c=c+1;
            }
        }
        return a;
    }
}