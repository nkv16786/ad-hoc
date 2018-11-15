try{
$usage= Get-WmiObject win32_processor -computername localhost | select DeviceID,LoadPercentage -ErrorAction Stop
$count = 1
$cpu_usage = @{}
foreach ($value in $usage){
$cpu_usage.Add($usage[$count-1].DeviceID, $usage[$count-1].LoadPercentage)
$count = $count+1
}
$output = @{"output" = $cpu_usage; "additional_attributes" = $cpu_usage}
return $output | convertto-json

}
catch{
$Errmsg = $_.Exception.Message
$err = "Command Failed:"+$Errmsg
$err1 = @{"Error" = $err}
return $err1 | ConvertTo-Json

}
