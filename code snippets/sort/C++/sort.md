### Sort vectors in ascending order of second element

```C++
# include <algorithm>
sort(vec0.begin(), vec0.end(), [](auto vec1, auto vec2) { 
		return (vec1[1] < vec2[1]); // using lambda expression
	});
```
