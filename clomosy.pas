var 
Myform:TclForm;
btnLedControl:TCLButton;
MyMqtt:TclMqtt;
ledOnOff:Boolean;
procedure btnLedControlClick;
begin
      if ledOnOff then
        MyMqtt.Send('ONRED')
      else
        MyMqtt.Send('OFFRED');
    ledOnOff:= Not ledOnOff;
end;
begin
      Myform:=TclForm.Create(Self);
      btnLedControl:=Myform.AddNewButton(Myform,'btnLedControl','Led On/Off');
      MyMqtt:=Myform.AddNewMqttConnection(Myform,'MyMqtt');
      MyMqtt.Channel:='LEDONOFF';
      MyMqtt.Connect;
      Myform.AddNewEvent(btnLedControl,tbeOnClick,'btnLedControlClick');
      ledOnOff:=True;
      Myform.Run;
end;
