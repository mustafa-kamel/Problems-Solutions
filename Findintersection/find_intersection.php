<?php

/**
 * [Returns the intersection of the two strings in the array as a comma separated string]
 * @param [mixed] $strArr [Input Array]
 * @return  [string] [string of comma seprated intersections charactes or false]
 */
function FindIntersection($strArr) {
  $str1 = explode(', ', $strArr[0]);
  $str2 = explode(', ', $strArr[1]);
  $intersect = '';
  foreach($str1 as $chr) {
    if (in_array($chr, $str2)) {
      $intersect .= $chr . ',';
    }
  }
  return $intersect ? substr($intersect, 0, strlen($intersect) -1) : 'false';

}
   
// keep this function call here  
// echo FindIntersection(fgets(fopen('php://stdin', 'r')));
echo FindIntersection(fgets(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]));

?>