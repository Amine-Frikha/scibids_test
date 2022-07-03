import { useEffect, useState } from "react";
import FormatObject from "./FormatObject";
import Loading from "./Loading";
function App() {
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [documents, setDocuments] = useState([]);
  useEffect(() => {
    fetch("/fulldocs")
      .then((res) => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setDocuments(
            result.data
              .filter((document) => document.name === "Scibids")
              .map((document) =>
                document.is_serious === 1
                  ? { ...document, is_serious: "Yes" }
                  : { ...document, is_serious: "No" }
              )
          );
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      );
  }, []);
  const oldVer = documents.filter((document) => document.version === 1)[0];

  const newVer = documents.filter((document) => document.version === 2)[0];

  if (error) {
    return <div>Error: {error.message}</div>;
  } else if (!isLoaded) {
    return <Loading />;
  } else {
    return (
      <div className="h-screen w-full flex flex-col justify-center items-center bg-gray-100 space-y-5 text-xl">
        <span>
          Name : <FormatObject oldVer={oldVer.name} newVer={newVer.name} />
        </span>
        <span>
          Number of employees :
          <FormatObject
            oldVer={oldVer.number_of_employees}
            newVer={newVer.number_of_employees}
          />
        </span>
        <span>
          Is Serious :
          <FormatObject oldVer={oldVer.is_serious} newVer={newVer.is_serious} />
        </span>
        <span className="space-x-2">
          Tags: <FormatObject oldVer={oldVer.tags[0]} newVer={newVer.tags[0]} />
          <FormatObject oldVer={oldVer.tags[1]} newVer={newVer.tags[1]} />
        </span>
      </div>
    );
  }
}

export default App;
