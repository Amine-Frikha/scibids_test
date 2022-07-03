import React from "react";

function FormatObject(props) {
  if (props.oldVer === props.newVer) {
    return <span>{props.oldVer}</span>;
  } else {
    return (
      <span className="space-x-2">
        <span className="font-bold">{props.newVer}</span>
        <span className="line-through">{props.oldVer}</span>
      </span>
    );
  }
}
export default FormatObject;
