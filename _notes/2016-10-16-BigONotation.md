---
title: "Big O Notation / Asymptotic Notation"
layout: single
author_profile: true
read_time: true
comments: true
share: true
related: true
categories:
  - Misc
tags:
  - Misc

---

Big O notation is a measure of how well an algorithm scales, with larger data  sets.

Measures the most complex part of algorithm, discards the parts that have very little effect once you get up to a very large data set. For instance in the equation: x = 45n^3 + 20n^2 + 19 once n > 100 the "+ 19" becomes _irrelevant_ to the outcome and once n is even bigger even the "20n^2" part becomes _irrelevant_, so the order become O(n^3).


## O(1)


```c#
void addItemToArray(int newItem)
{
	theArray[itemsInArray++] = newItem;
}
```

Not matter what size the array is, this will take the same amount of time to execute.

## O(n)

```c#
void linearSearch(int itemToFind)
{
	bool found = false;
	for(int i = 0; i < itemsInArray; i++)
  	{
    	if (theArray[i] == itemToFind)
      		found = true;
      		break;
  	}
}
```

 Has to go through every item in the array at least once (worse case), the efficiency of the algorithm is directly proportional to the size of the data set.

## O(n^2), O(n^3) ...

```c#
void bubbleSort()
{
	for (int i = arraySize - 1; i > 1; i--) 
	{
  		for (int j = 0; j < i; j++) 
    	{
    		if (theArray[j] > theArray[j+1])
	  			swapValues(j, j+1);
	  	}
	}
}
```

Nested loop, so the main loop is order of O(n) and then the nested loop is also O(n), as such the whole algorithm is O(nn) = O(n^2).  Therefore for algorithms with more nested loops the exponent would increase, i.e. 3 nested loops has an order of O(n^3).

## O(log N)

```c#
void binarySearch(int itemToFind)
{
	int lowIndex = 0;
  	int highIndex = arraySize - 1;
  
  	while (lowIndex <= highIdex) {
    	int middleIndex = (highIndex + lowIndex) / 2;
      	
      	if (theArray[middleIndex] < itemToFind)
          	lowIndex = middleIndex + 1;
      	else if (theArray[middleIndex] > value)
          	highIndex = middleIndex - 1;
      	else
        {
        	print("Match found at " + middleIndex);
          	break;
        }
  	}
}
```

Here there is only one loop through the data, similar to O(n) but the data being looped through is decreased by roughly 50% each iteration this makes it O(logN) which is much more effecient than O(n).

## O(n log n)

```c#
void quickSort(int left, int right)
{
 	if (right - left <= 0) return
    else
    {
      	int pivot = theArray[right];
      	int pivotLocation = partitionArray(left, right, pivot);
      	quickSort(left, pivotLocation - 1);
      	quickSort(pivotLocation + 1, right);
    }
}

int partionArray(int left, int right, int pivot)
{
  	int leftPoint = left - 1;
  	int rightPoint = right;
  
  	while(true)
    {
      	while(theArray[++leftPoint] < pivot)
          	;
        print("theArray[leftPoint] is bigger than the pivot value");
        while(rightPoint > 0 && theArray[--rightPoint] > pivot)
          	;
        print("theArray[rightPoint] is smaller than the pivotValue");
        if (leftPoint >= rightPoint)
          	break;
     	else
          	swap(leftPoint, rightPoint);
    }
  
  	swap(leftPoint, right);
  	return leftPoint;
}
```

The number of comparisons is equal to log(n)! which equals nlog(n).
