class Solution {
    public int solution(int[] sides) {
        int max= sides[0];
        int sum=0;
        
        for(int i=0; i<sides.length; i++){
            if(sides[i]>max){
                max=sides[i];
            }
            sum+=sides[i];
        }
          return (max < sum - max) ? 1 : 2;
    }
}