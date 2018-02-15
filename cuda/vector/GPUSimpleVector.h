//  author: Felice Pantaleo, CERN, 2018
#ifndef GPU_SIMPLEVECTOR_H_
#define GPU_SIMPLEVECTOR_H_

#include <cuda.h>
#include <type_traits>


namespace GPU {
template <class T> struct SimpleVector {
  // Constructors
  __host__ __device__ SimpleVector(int capacity, T *data)
      : m_size(0), m_data(data), m_capacity(capacity) {
          static_assert(std::is_trivially_destructible<T>::value);
      }

  __host__ __device__ SimpleVector() : SimpleVector(0) {}

  __inline__ __host__ __device__ int push_back(const T &element) {
    auto previousSize = m_size;
    m_size++;
    if (previousSize < m_capacity) {
      m_data[previousSize] = element;
      return previousSize;
    } else {
      --m_size;
      return -1;
    }
  }


  template <class... Ts>
  __host__ __device__
  void emplace_back(Ts&&... args) {
      auto previousSize = m_size;
      m_size++;
      if (previousSize < m_capacity) {
        (new (&m_data[previousSize]) T(std::forward<Ts>(args)...));
        return previousSize;
      } else {
        --m_size;
        return -1;
      }
    }


  __inline__ __host__ __device__ T& back() const {

    if (m_size > 0) {
      T& ref = m_data[m_size - 1];
      return ref;
    } else
      return T();
  }


#if defined(__NVCC__) || defined(__CUDACC__)
// thread-safe version of the vector, when used in a CUDA kernel
  __device__ int push_back_ts(const T &element) {
    auto previousSize = atomicAdd(&m_size, 1);
    if (previousSize < m_capacity) {
      m_data[previousSize] = element;
      return previousSize;
    } else {
      atomicSub(&m_size, 1);
      return -1;
    }
  }
#endif

  __inline__ __host__ __device__ T operator[](int i) const { return m_data[i]; }

  __inline__ __host__ __device__ void reset() { m_size = 0; }

  __inline__ __host__ __device__ int size() const { return m_size; }

  __inline__ __host__ __device__ int capacity() const { return m_capacity; }

  __inline__ __host__ __device__ T* data() const { return m_data; }

private:
  int m_size;
  int m_capacity;

  T *m_data;
};
} // namespace GPU

#endif
