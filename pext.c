#include "c2.h"
#include "tlv.h"

static c2_api_call_t pext_test(tlv_transport_pkt_t tlv_transport_packet)
{
    return craft_c2_api_call_pkt(tlv_transport_packet.tlv_transport_pkt_tag,
                                 API_CALL_FAIL, "test");
}

void load(c2_api_calls_t **c2_api_calls_table)
{
    c2_register_api_call(c2_api_calls_table, c2_api_call_tag(1), pext_test);
}
