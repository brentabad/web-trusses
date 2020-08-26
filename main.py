from flask import Flask
from flask_restful import Api, Resource, reqparse
import numpy as np

app = Flask(__name__)
api = Api(app)

input_args = reqparse.RequestParser()
input_args.add_argument("matrixA", type=str)
input_args.add_argument("matrixB", type=str)


def matrix(matrixA, matrixB):
    arrA = np.array(matrixA)
    arrB = np.array(matrixB)
    print(arrA)
    print(arrB)
    arrC = np.add(arrA, arrB)
    print(arrC)
    return arrC


class MatrixDet(Resource):
    def put(self, input):
        args = input_args.parse_args()

        matA = args['matrixA']
        matB = args['matrixB']

        matA = matA.split(',')
        matB = matB.split(',')

        matA = [int(i) for i in matA]
        matB = [int(i) for i in matB]

        answer = matrix(matA, matB)
        answer = str(answer).strip('[]')
        return {"answer": answer}


api.add_resource(MatrixDet, "/matrix/<int:input>")

if __name__ == "__main__":
    app.run(debug=True)
