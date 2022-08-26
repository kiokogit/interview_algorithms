//see whether you can reacch the end

//cases
/* 
1. empty array [] - true
2. array with single element [0] [2] - @returns true
3. array with zero at start and non-zeros after [0,5,2,1,0] - false
4. array where lands at zero with non-zero after [1,0,3,5] - false but [2,0,3,5] - true

*/


function reach_the_end(arr=[]){

    //base case
    if (arr.length <= 1){
        return true
    }
    
    let currentStep = 0

    while (currentStep <=arr.length-1){
        if(arr[currentStep]===0){
            if(arr.slice(currentStep).some(num=>num > 0)){
                return false
            } 
            else {
                break
            }
        }
        // add the current step index to the value of the index arr[index]
        // to get the next step
        currentStep = currentStep + arr[currentStep]
    }
    return true
}

console.log(reach_the_end([8,5,1]))