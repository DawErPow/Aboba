#Первое задание
Function aboba() {
  Return "hello world!"
}
#Второе задание
function CheckForFactor([int] $base, [int] $factor) {
  !($base%$factor)
}
      
#Третие задание
function TerminalMove([int] $pos, [int] $roll) {
  return $pos + 2 * $roll;
}

#Четвертое задание
function stayHydratred($time){
  return [math]::floor($time/2)
}
      
#Пятое задание
function nb-dig($n, $d)
{
    return [regex]::Matches(-join (0..$n).ForEach({ $_ * $_ }),"$d").count
}
      
#Шестое задание
function overTheRoad($address, $n) {
  return $n * 2 - $address + 1;
}
      
#Седьмое задание
function Angle([int] $n) {
  180 * ($n - 2)
}  
#Восьмое задание
   function Last-Survivor([string]$letters, [int[]]$numbers)
{
  foreach ($number in $numbers) {
    $letters = $letters.remove($number, 1)
  }
  $letters
}
#Девятое задание
function Get-EvenOrOdd($number) {
  if ($number % 2 -eq 0) {return 'Even'}
  return 'Odd'
}

#Десятое задание
function Summation([int] $n) {
  return ($n + 1) * $n / 2
}
