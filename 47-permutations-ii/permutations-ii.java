class Solution {
    public void form(int[] nums,int start,int size,List<List<Integer>>result){
        if(start == size){  
            List<Integer> ans = new ArrayList<>();
            for (int ele : nums) ans.add(ele);
            result.add(ans);
            return;
        }

        HashSet<Integer> set = new HashSet<>();
        for(int i =start;i<size;i++){
            if(set.contains(nums[i])) continue;

            set.add(nums[i]);
            int temp = nums[start];
            nums[start] = nums[i];
            nums[i] = temp;

            form(nums,start+1,size,result);

            temp = nums[start];
            nums[start] = nums[i];
            nums[i] = temp;
        }
    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        int n = nums.length;
        List<List<Integer>> result = new ArrayList<>();        
        form(nums,0,n,result);
        return result;
    }
}