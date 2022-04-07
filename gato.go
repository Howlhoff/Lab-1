//------------------------gato.go-----------------------------
//TODO: Literal todo
//------------------------------------------------------------

package gato

import (
	"fmt"
	"math/rand"
	"time"
	"log"
	"net"
)


func checkError(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func main() {
	rand.Seed(time.Now().Unix())
	conexion, errores = net.Dial("tcp","localhost:5002")
	checkError(errores)
	defer conexion.Close()

}
